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
            { "data": "full_name"},
            
            { "data": "username"},
            { "data": "email" },
            // { "data": "equipo_nombre" },
            { "data": "groups"},
            { "data": "image"},
            { "data": "id"},

            
            ],
        columnDefs: [
                {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/edit/'+row.id+'/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/user/delete/'+row.id+'/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                },
                
    },
    {
        targets: [-2],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
            return '<img src="'+row.image+'" class="img-fluid mx-auto d-block" style="width: 20px; height: 20px;">';
        },
    },

    {
        targets: [-3],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
            var html = '';
            $.each(row.groups, function (key, value){
                html+='<span class="badge badge-success">'+value.name+'</span> ';

            });
            return html;
        },
    },
],
initComplete: function(settings, json) {
  }
});
});