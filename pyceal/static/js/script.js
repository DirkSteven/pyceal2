const printBtn = document.getElementById('print');
const image = document.getElementById('myImage');

printBtn.addEventListener('click', function() {
    printImage();
});


function printImage() {
    let printWindow = window.open('', 'Print Window');
    printWindow.document.write('<html><head><title>Image Preview</title>');
    printWindow.document.write('<style>img {max-width: 80%; height: auto;}</style>');
    printWindow.document.write('</head><body><img src="' + image.src + '"></body></html>');
    printWindow.document.close();
    printWindow.focus();
    printWindow.print();
    printWindow.close();
    window.location.reload();
}

