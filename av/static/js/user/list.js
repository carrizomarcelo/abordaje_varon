$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
                },
            dataSrc: "",
            },
        columns: [
            { "data": "position"},
            { "data": "last_name"},
            { "data": "first_name"},
            { "data": "user_depto_id_id"},
            { "data": "date_joined" },
            { "data": "date_joined"},
            ],
        columnDefs: [
                {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/update'+row.id+'/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/user/delete'+row.id+'/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                },
    },
],
initComplete: function(settings, json) {
  }
});
});