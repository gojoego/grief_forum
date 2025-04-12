function togglePost(id) {
    const body = document.getElementById('body-' + id);
    if (body.style.display === 'none' || body.style.display === '') {
        body.style.display = 'block';
        body.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    } else {
        body.style.display = 'none'
    }
}