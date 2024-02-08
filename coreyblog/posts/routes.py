from flask import Blueprint

# create instance of Blueprint object 
posts = Blueprint('posts', __name__)



@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    # create instance of from
    form = PostForm()

    # rules for handling validated form when submitted
    if form.validate_on_submit():

        # add post to db
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()

        # flash message
        flash('Your post has been created', 'success')

        return redirect(url_for('home'))

    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):

    # 404 = page doesn;t exist
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required     # if you want to update a post, user required to be logged in
def update_post(post_id):
    # 404 = page doesn;t exist
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        # manually aborts and returns a http response 403 (forbidden route)
        abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post is updated', 'success')
        return redirect(url_for('post', post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post had been deleted', 'success')
    return redirect(url_for('home'))


