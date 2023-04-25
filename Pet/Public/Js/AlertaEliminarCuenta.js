function borrarusuario(id) {
    swal({
            title: "¿Estas seguro que quieres eliminar tu cuenta?",
            text: "Si eliminas la cuenta, no podras recuperarla despues",
            icon: "warning",
            buttons: ["Cancelar", true],
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {
                location.href = "/Usuarios/eliminar/" + id;
                swal("¡Tu cuenta se ha eliminado exitosamente!", {
                    icon: "success",
                });

            } else {
                swal("Se cancelo exitosamente");
            }
        });
}