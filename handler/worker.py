class Worker:
    def __init__(self):
        pass

    def process_request(self, request):
        task = request['task']
        kwargs = request['args']

        if task == 'classify-text':
            response = self._classify_text(**kwargs)
        elif task == 'generate-text':
            response = self._generate_text(**kwargs)
        elif task == 'transform-text':
            response = self._transform_text(**kwargs)
        else:
            raise ValueError('Unknown task "{}"'.format(task))

        return response

    def _classify_text(self, text, **kwargs):
        # TODO
        return {
            "probs": [0, 0.5, 1.0, 0.3]
        }

    def _generate_text(self, label, **kwargs):
        # TODO
        return {
            "text": 'Are you in pain, Frodo?'
        }

    def _transform_text(self, text, label, **kwargs):
        # TODO
        return {
            "text": text
        }
