from pprint import pprint

from flask import Flask, request

# from graph_compile import rag_app

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
# @app.route('/handle_request', methods=['POST'])
# def handle_request():
#     result ={}
#     data = request.get_json()
#     print(data)
#     question = data.get('question')
#     print(question)
#     # inputs = {
#     #     "question": "What player at the Bears expected to draft first in the 2024 NFL draft?"
#     # }
#     for output in rag_app.stream(data):
#         for key, value in output.items():
#             # Node
#             pprint(f"Node '{key}':")
#             # Optional: print full state at each node
#             # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
#         pprint("\n---\n")
#
#     # Final generation
#     pprint(value["generation"])
#     result['answer'] = value["generation"]
#     return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)