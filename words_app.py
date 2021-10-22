from flask import Flask, request
import logging
from rq import Queue

from worker import conn

from redis_utils.handle_messages import query_all_messages, worker_save_message

app = Flask(__name__)
q = Queue(connection=conn)


@app.route('/post', methods=['GET', 'POST'])
def post_message():
    if request.method == "POST":
        logging.info('new post message request received')
        message = request.json.get('message')
        if not message:
            return "BadRequest: post must include a message", 400
        job = q.enqueue_call(
            worker_save_message,[message]
        )
        logging.info(f"new post message job enqueue, message={message}, job_id={job.get_id()}")

        return "message added to queue", 201


@app.route("/getall", methods=['GET'])
def get_results():
    logging.info('new get all posted message request received')
    posted_messages: list[str] = query_all_messages()

    # parse the posted messages into a single string, joined by newline as required in the assignment
    ready_to_send_posted_messages = '\n'.join(posted_messages)

    return ready_to_send_posted_messages, 200


if __name__ == '__main__':
    app.run()