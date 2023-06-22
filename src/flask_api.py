import logging
import waitress
from flask import Flask, make_response, request
from flask_restx import Resource, Api, model, fields


def create_flask_api(logger: logging.Logger):
    api = Api()
    app = Flask(__name__)
    api.init_app(app, title="Beans Coatings API", description="API for Beans Coatings Web")

    @api.route('/health', endpoint='health')
    @api.doc(params={}, description='Health endpoint')
    class Health(Resource):
        @api.doc(responses={200: 'Alive and well',
                            500: 'Problem!'})
        def get(self):
            logger.log(69, "responding to request on: \'{}\' from client: \'{}\'".format('/health',
                                                                                         request.remote_addr))
            return make_response("Alive and well", 200)

    # app.run(host="0.0.0.0", debug=True, use_reloader=False)
    waitress.serve(app, host="0.0.0.0", port=5000)
