$('#myTable').DataTable({
    pageLength: 10,
    ajax: "/data",
    columns: [
        { data: 5 },
        { data: 0 },
        { data: 1 },
        { data: 2 },
        { data: 3 },
        { data: 4 },
    ]
});