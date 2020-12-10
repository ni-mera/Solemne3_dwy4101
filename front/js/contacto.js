$(document).ready(function(){
    ValidaSoloTxt('#txtNombre');
    ValidaSoloTxt('#txtApellido');
    ValidaSoloNumber('#contactNumber');
    $('#formContacto')
    .validate({
        errorElement: 'span',
        errorPlacement: function (error, element) {
            error.addClass('invalid-feedback');
            element.closest('.form-group').append(error);
        },
        highlight: function (element, errorClass, validClass) {
            $(element).addClass('is-invalid');
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).removeClass('is-invalid').addClass('is-valid');
        },
        rules: {
            txtNombre: {               
                minlength: 3,
                required: true
            },
            txtApellido: {
                minlength: 3,
                required: true
            },
            txtEmail: {
                required: true,
                email: true
            },
            contactNumber:{
                minlength: 9,
                required: true
            },
            txtMensaje: {
                minlength: 10,
                required: true
            }
        },
        messages: {
            txtNombre: {
                required: 'El campo de nombre es requerido',
                minlength: 'Ingrese un nombre válido'
            },
            txtApellido: {
                required: 'El campo de apellido es requerido',
                minlength: 'Ingrese un apellido válido'
            },
            txtEmail: {
                required: 'El campo de correo es requerido',
                email: 'El campo de correo no tiene un formato válido de correo'
            },
            contactNumber: {
                required: 'Su N° de contacto es requerido',
                minlength: 'El campo requiere 9 dígitos'
            },
            txtMensaje: {
                required: 'El campo motivo de contacto es obligatorio',
                minlength: 'Ingrese su motivo de contacto'
            }
        }
    });
});

function ValidaSoloTxt(inputId){
    $(function () {
        $(inputId).keydown(function (e) {
            if (e.shiftKey || e.ctrlKey || e.altKey) {
                e.preventDefault();
            } else {
                var key = e.keyCode;
                if (!((key == 8) || (key == 32) || (key == 46) || (key >= 35 && key <= 40) || (key >= 65 && key <= 90))) {
                    e.preventDefault();
                }
            }
        });
    });
}

function ValidaSoloNumber(inputId){
    $(inputId).keypress(function (e) {
        if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
            e.preventDefault();
        }
    });
}