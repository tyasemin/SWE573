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
            'label': node.title,
            'description': node.description or '',
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

        Node.objects.create(
            title=title,
            description=description,
            wikidata_description=request.POST.get('wikidata_description'),
            board=board,
            created_by=request.user
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
