document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    var formData = new FormData();
    formData.append('file', document.getElementById('file-input').files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = 'DNA Sequence: ' + data.dna_sequence;
    })
    .catch(error => console.error('Error:', error));
});