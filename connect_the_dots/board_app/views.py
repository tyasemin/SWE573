import json
from django.shortcuts import render, get_object_or_404
from db.models import Board
from db.models import Node
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from db.models import Connection

from django.core.serializers.json import DjangoJSONEncoder
import json

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    nodes = board.nodes.all()
    connections = board.connections.all()

    node_data = [
        {
            'id': node.id,
            'label': node.label or node.title,
            'title': node.title,
            'description': node.description or '',
            'wikidata_id': node.wikidata_id,
            'wikidata_description': node.wikidata_description,
            'wikidata_image_url': node.wikidata_image_url or '',
            'wikidata_selected_properties': node.wikidata_selected_properties or {},
            'manual_properties': node.manual_properties or {},
            'connections': [
                {
                    'to': c.to_node.id,
                    'to_label': c.to_node.label or c.to_node.title,
                    'label': c.label
                }
                for c in node.outgoing_connections.all()
            ] + [
                {
                    'from': c.from_node.id,
                    'from_label': c.from_node.label or c.from_node.title,
                    'label': c.label
                }
                for c in node.incoming_connections.all()
            ]
        }
        for node in nodes
    ]

    edge_data = [
        {
            'from': connection.from_node.id,
            'to': connection.to_node.id,
            'label': connection.label,
        }
        for connection in connections
    ]

    context = {
        'board': board,
        'nodes_json': json.dumps(node_data, cls=DjangoJSONEncoder),
        'edges_json': json.dumps(edge_data, cls=DjangoJSONEncoder),
    }
    return render(request, 'board_app/board_detail.html', context)




@login_required
def add_node(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        board_id = request.POST.get('board_id')
        board = get_object_or_404(Board, id=board_id)

        import json
        manual_properties_raw = request.POST.get('manual_properties_json', '{}')
        try:
            manual_properties = json.loads(manual_properties_raw)
        except json.JSONDecodeError:
            manual_properties = {}

        # Wikidata properties
        wikidata_properties_raw = request.POST.get('wikidata_properties')
        try:
            wikidata_properties = json.loads(wikidata_properties_raw) if wikidata_properties_raw else {}
        except json.JSONDecodeError:
            wikidata_properties = {}

        # Node oluştur
        Node.objects.create(
            title=title,
            description=description,
            wikidata_description=request.POST.get('wikidata_description'),
            wikidata_image_url=request.POST.get('wikidata_image_url'),
            wikidata_id=request.POST.get('wikidata_id'),
            wikidata_selected_properties=wikidata_properties,
            board=board,
            created_by=request.user,
            manual_properties=manual_properties,
        )

        return redirect('board_detail', board_id=board.id)
    

@login_required
def add_connection(request):
    if request.method == "POST":
        from_node = Node.objects.get(id=request.POST["from_node_id"])
        to_node = Node.objects.get(id=request.POST["to_node_id"])
        label = request.POST["label"]
        Connection.objects.create(
            from_node=from_node,
            to_node=to_node,
            label=label,
            board=from_node.board,
            created_by=request.user
        )
        return redirect('board_detail', board_id=from_node.board.id)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from db.models import Node

@csrf_exempt  
def delete_node(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            node_id = data.get("node_id")
            if node_id:
                Node.objects.filter(id=node_id).delete()
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"error": "Missing node_id"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=405)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from db.models import Connection  

@csrf_exempt
def delete_connection(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            conn_id = data.get('connection_id')
            if conn_id:
                Connection.objects.filter(id=conn_id).delete()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'error': 'Missing connection_id'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=405)

@csrf_exempt
@login_required
def update_node(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            node = Node.objects.get(id=data['id'])

            
            node.manual_properties = data.get('manual_properties', node.manual_properties)

            
            if 'wikidata_selected_properties' in data:
                node.wikidata_selected_properties = {}

            node.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=405)