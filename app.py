from flask import Flask, render_template, request
import config
import aicontent

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Generate a detailed Product Description for: {}".format(submission)
        openAIAnswer = aicontent.OpenAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
        
    return render_template('product-description.html', **locals())



@app.route('/job-description', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        submission = request.form['jobDescription']
        query = "Generate a detailed Job Description for: {}".format(submission)
        openAIAnswerUnformated = aicontent.OpenAIQuery(query)
        openAIAnswer = openAIAnswerUnformated.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('job-description.html', **locals())



@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas():

    if request.method == 'POST':
        submission = request.form['tweetIdeas']
        part1 = aicontent.OpenAIQuery("Generate a tweet on the subject: {} \n".format(submission))
        part2 = aicontent.OpenAIQuery('Generate twitter hashtag for: {}'.format(submission))

        openAIAnswer = '{} {}'.format(part1, part2)
        prompt = 'AI Suggestions for {} are:'.format(submission)
    return render_template('tweet-ideas.html', **locals())



@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
        submission = request.form['coldEmails']
        query = "Write a cold email to potential clients about: {}".format(submission)
        openAIAnswerUnformated = aicontent.OpenAIQuery(query)
        openAIAnswer = openAIAnswerUnformated.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('cold-emails.html', **locals())



@app.route('/social-media', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        submission = request.form['socialMedia']
        query = "Generate a Facebook Ad copy for our product: {}".format(submission)
        openAIAnswerUnformated = aicontent.OpenAIQuery(query)
        openAIAnswer = openAIAnswerUnformated.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('social-media.html', **locals())


@app.route('/business-pitch', methods=["GET", "POST"])
def businessPitch():

    if request.method == 'POST':
        submission = request.form['businessPitch']
        query = "Generate a Business idea Pitch for: {}".format(submission)
        openAIAnswerUnformated = aicontent.OpenAIQuery(query)
        openAIAnswer = openAIAnswerUnformated.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('business-pitch.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas():

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Generate a Youtube video topic ideas for: {}".format(submission)
        openAIAnswerUnformated = aicontent.OpenAIQuery(query)
        openAIAnswer = openAIAnswerUnformated.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"])
def videoDescription():

    if request.method == 'POST':
        submission = request.form['videoDescription']
        query = "Generate a detailed Youtube Video Description for: {}".format(submission)
        openAIAnswerUnformated = aicontent.OpenAIQuery(query)
        openAIAnswer = openAIAnswerUnformated.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('video-description.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
