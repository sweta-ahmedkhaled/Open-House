document.addEventListener('DOMContentLoaded', function() {
    // Previous code remains the same until the form submission...

    // Form submission with fetch API
    const reservationForm = document.getElementById('reservationForm');
    const reservationSuccess = document.getElementById('reservationSuccess');
    
    reservationForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (this.checkValidity()) {
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                guests: document.getElementById('guests').value,
                date: document.getElementById('date').value,
                time: document.getElementById('time').value,
                specialRequests: document.getElementById('specialRequests').value
            };

            // Send data to server
            fetch('http://localhost:3001/api/reservations', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                reservationSuccess.classList.remove('d-none');
                reservationForm.reset();
                reservationForm.classList.remove('was-validated');
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    reservationSuccess.classList.add('d-none');
                }, 5000);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('There was an error submitting your reservation. Please try again.');
            });
        } else {
            this.classList.add('was-validated');
        }
    });

    // Rest of your existing code...
});


document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Menu filtering
    const filterButtons = document.querySelectorAll('[data-filter]');
    const menuItems = document.querySelectorAll('.menu-item');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            const filterValue = this.getAttribute('data-filter');
            
            // Filter menu items
            menuItems.forEach(item => {
                if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    // Shopping cart functionality
    const cart = [];
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const orderItemsElement = document.getElementById('orderItems');
    const orderTotalElement = document.getElementById('orderTotal');
    const orderModal = new bootstrap.Modal(document.getElementById('orderModal'));
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.card');
            const title = card.querySelector('.card-title').textContent;
            const price = parseFloat(card.querySelector('.price').textContent.replace('$', ''));
            
            cart.push({ title, price });
            updateCart();
            orderModal.show();
        });
    });
    
    function updateCart() {
        orderItemsElement.innerHTML = '';
        let total = 0;
        
        cart.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'd-flex justify-content-between mb-2';
            itemElement.innerHTML = `
                <span>${item.title}</span>
                <span>$${item.price.toFixed(2)}</span>
            `;
            orderItemsElement.appendChild(itemElement);
            total += item.price;
        });
        
        orderTotalElement.textContent = `$${total.toFixed(2)}`;
    }

    // Form validation
    const reservationForm = document.getElementById('reservationForm');
    const reservationSuccess = document.getElementById('reservationSuccess');
    
    reservationForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (this.checkValidity()) {
            // In a real app, you would send this data to a server
            reservationSuccess.classList.remove('d-none');
            reservationForm.reset();
            reservationForm.classList.remove('was-validated');
            
            // Hide success message after 5 seconds
            setTimeout(() => {
                reservationSuccess.classList.add('d-none');
            }, 5000);
        } else {
            this.classList.add('was-validated');
        }
    });

    // Set minimum date for reservation to today
    const dateInput = document.getElementById('date');
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
    
    // Initialize carousel with interval
    const heroCarousel = new bootstrap.Carousel(document.getElementById('heroCarousel'), {
        interval: 5000,
        ride: 'carousel'
    });
});