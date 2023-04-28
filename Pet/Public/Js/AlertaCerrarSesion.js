function cerrarusuario(id) {
    swal({
            title: "¿Estas seguro de cerrar sesion?",
            text: "",
            icon: "warning",
            buttons: ["Cancelar", true],
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {
                location.href = "" + id;
                swal("", {
                    icon: "success",
                });

            } else {
                swal("Se cancelo exitosamente");
            }
        });
}