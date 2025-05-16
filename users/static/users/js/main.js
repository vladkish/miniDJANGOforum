document.addEventListener('DOMContentLoaded', function() {
    const avatarInput = document.querySelector('.upload-btn-wrapper input[type="file"]');
    if (avatarInput) {
        avatarInput.addEventListener('change', function(e) {
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const previewImg = document.querySelector('.avatar-preview img');
                    if (previewImg) {
                        previewImg.setAttribute('src', e.target.result);
                    }
                }
                reader.readAsDataURL(this.files[0]);
            }
        });
    }

    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            
            const linkText = this.textContent.trim();
            console.log(`Переход на: ${linkText}`);
        });
    });

    const showRegister = document.getElementById('show-register');
    const showLogin = document.getElementById('show-login');
    
    if (showRegister && showLogin) {
        showRegister.addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById('login-form').classList.add('hidden');
            document.getElementById('register-form').classList.remove('hidden');
            document.getElementById('register-form').classList.add('active-form');
        });
        
        showLogin.addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById('register-form').classList.add('hidden');
            document.getElementById('login-form').classList.remove('hidden');
            document.getElementById('login-form').classList.add('active-form');
        });
    }
});