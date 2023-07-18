document.addEventListener('DOMContentLoaded', function() {
    var changeColorBtn = document.getElementById('changeColorBtn');
    changeColorBtn.addEventListener('click', function() {
        var body = document.querySelector('body');
        body.classList.toggle('dark-mode');
    });

    var fileInput = document.getElementById('file');
    var fileInputLabel = document.getElementById('fileInputLabel');
    var uploadBtn = document.getElementById('uploadBtn');
    var processedImageContainer = document.getElementById('processedImageContainer');


window.addEventListener("DOMContentLoaded", (event) => {
    fileInputLabel.addEventListener('click', function() {
        fileInput.click();
    });
  });

    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            uploadBtn.style.display = 'block';
        } else {
            uploadBtn.style.display = 'none';
        }
    });

    uploadBtn.addEventListener('click', function() {
        var form = document.getElementById('uploadForm');
        form.submit();
    });

    if (processedImageContainer.querySelector('.processed-image')) {
        processedImageContainer.style.display = 'block';
    }

    
});


console.log(1);

// document.addEventListener('DOMContentLoaded', function() {
//
// });


// Script for the "Change Color" button
document.addEventListener('DOMContentLoaded', function() {
    var changeColorBtn = document.getElementById('changeColorBtn');
    changeColorBtn.addEventListener('click', function() {
        var processedImage = document.querySelector('.processed-image');
        processedImage.classList.toggle('dark-mode');
    });
});
