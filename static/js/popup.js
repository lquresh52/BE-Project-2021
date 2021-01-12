// Inline popups
$('#inline-popups').magnificPopup({
    delegate: 'a',
    removalDelay: 500, //delay removal by X to allow out-animation
    callbacks: {
      beforeOpen: function() {
         this.st.mainClass = this.st.el.attr('data-effect');
      }
    },
    midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
  });
  

  
  

  

  // Function for checking the validation of the form elements.
// It checks First Name, Last Name, Email and Phone Number for the Sign Up Form
(function() {
    'use strict';
    window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
            if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
                document.getElementById('loader').style.display = 'none';
            }
            if (form.checkValidity() === true){
              document.getElementById('loader').style.display = 'block';
            }
            form.classList.add('was-validated');
        }, false);
    });
    }, false);
    })();