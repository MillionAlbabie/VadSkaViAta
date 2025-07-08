from flask import Blueprint, render_template, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Startsida"""
    return '''
    <h1>VadSkaViAta</h1>
    <p>Välkommen till din måltidsplaneringsapp!</p>
    <ul>
        <li><a href="/api/health">API Health Check</a></li>
        <li><a href="/api/foods">Visa alla maträtter</a></li>
    </ul>
    '''

@bp.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'OK',
        'message': 'VadSkaViAta API is running',
        'version': '1.0.0'
    })

@bp.route('/api/foods')
def get_foods():
    """Visa alla maträtter (tillfälligt utan databas)"""
    # Tillfällig data tills vi skapar modeller
    sample_foods = [
        {
            'id': 1,
            'name': 'Pasta Carbonara',
            'cuisine_type': 'italiensk',
            'difficulty': 'medium'
        },
        {
            'id': 2,
            'name': 'Köttbullar med potatismos',
            'cuisine_type': 'svensk',
            'difficulty': 'easy'
        }
    ]
    return jsonify(sample_foods)