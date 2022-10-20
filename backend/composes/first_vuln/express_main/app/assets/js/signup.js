document.getElementById('form').addEventListener('submit', e => {
  e.preventDefault();
    fetch('/api/signup', {
      method: 'POST',
      body: JSON.stringify({
        'email': document.querySelector('input[type=email]').value,
        'name' : document.querySelector('input[type=text]').value,
        'password' : document.querySelector('input[type=password]').value
        }),
        headers: {'Content-Type': 'application/json'}
      }).then(resp => {
        return resp.json();
    }).then(data => {
      document.getElementById('output').innerHTML = data.response;
  });
});
