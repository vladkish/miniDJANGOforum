document.getElementById('id_image').addEventListener('change', function(e) {
    const preview = document.getElementById('image-preview');
    const file = e.target.files[0];
    
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        }
        
        reader.readAsDataURL(file);
    }
});

const uploadLabel = document.querySelector('.image-upload-label');

uploadLabel.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadLabel.style.borderColor = '#3498db';
    uploadLabel.style.backgroundColor = '#f0f7fc';
});

uploadLabel.addEventListener('dragleave', () => {
    uploadLabel.style.borderColor = '#e0e0e0';
    uploadLabel.style.backgroundColor = '';
});

uploadLabel.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadLabel.style.borderColor = '#e0e0e0';
    uploadLabel.style.backgroundColor = '';
    
    const fileInput = document.getElementById('id_image');
    fileInput.files = e.dataTransfer.files;
    
    const event = new Event('change');
    fileInput.dispatchEvent(event);
});