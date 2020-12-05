var jQueryScript = document.createElement('script');  
jQueryScript.setAttribute('src','https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js');
document.head.appendChild(jQueryScript);


var animation = bodymovin.loadAnimation({
    container: document.getElementById('lottie'), // Required
    path: "/static/js/data.json", // Required
    renderer: 'svg', // Required
    loop: true, // Optional
    autoplay: true, // Optional
    name: "Hello World", // Name for future reference. Optional.
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
              document.getElementById('loaderLogin').style.display = 'none';
              document.getElementById('loader').style.display = 'none';
          }
          if (form.checkValidity() === true){
            document.getElementById('loaderLogin').style.display = 'block';
            document.getElementById('loader').style.display = 'block';
          }
          form.classList.add('was-validated');
      }, false);
  });
  }, false);
  })();

// $(document).ready(function(){
//   // ------------ Check passwords similarity --------------
//   $('#validationPassword, #validationConfirmPassword').on('keyup', function () {
//     if ($('#validationPassword').val() != '' && 
//         $('#validationConfirmPassword').val() != '' && 
//         $('#validationPassword').val() == $('#validationConfirmPassword').val()){
//           $('#cPwdValid').show();
//           $('#cPwdInvalid').hide();
//           $('#cPwdInvalid').html('Passwords Match').css('color', 'green');
//           $('.myCpwdClass').addClass('is-valid');
//           $('.myCpwdClass').removeClass('is-invalid');
//           $("#submitBtn").attr("disabled",false);
//           $('#submitBtn').addClass('btn-primary').removeClass('btn-secondary');
//           for (i = 0; i < myInputElements.length; i++) {
//             var myElement = document.getElementById(myInputElements[i].id);
//             if (myElement.classList.contains('is-invalid')) {
//               $("#submitBtn").attr("disabled",true);
//               $('#submitBtn').addClass('btn-secondary').removeClass('btn-primary');
//               break;
//             }
//           }
//     } else {
//           $('#cPwdValid').hide();
//           $('#cPwdInvalid').show();
//           $('#cPwdInvalid').html('Not Matching').css('color', 'red');
//           $('.myCpwdClass').removeClass('is-valid');
//           $('.myCpwdClass').addClass('is-invalid');
//           $("#submitBtn").attr("disabled",true);
//           $('#submitBtn').addClass('btn-secondary').removeClass('btn-primary');
//     }
//   });
// });    


