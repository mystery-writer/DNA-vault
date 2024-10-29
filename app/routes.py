from flask import Blueprint, render_template, request, jsonify
from .dna_utils import process_file

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        dna_sequence = process_file(file)
        return jsonify({'dna_sequence': dna_sequence})

@bp.route('/retrieve', methods=['POST'])
def retrieve_file():
    dna_sequence = request.json.get('dna_sequence')
    if not dna_sequence:
        return jsonify({'error': 'No DNA sequence provided'})
    
    # Implement file retrieval logic here
    # This is a placeholder
    return jsonify({'message': 'File retrieved successfully'})
