document.addEventListener("DOMContentLoaded",function (event){
    console.log("this is blog js");
    let sc = document.createElement('script')
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js');

    document.head.appendChild(sc);
    sc.onload = ()=>{
        // var useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
        tinymce.init({
            selector: '#id_content',
            height:656,

            plugins: 'image tools print textpattern preview code visualblocks visualchars link media emoticons directionality advlist lists wordcount insertdatetime quickbars',
            menubar: 'file edit view insert format tools table help',
            toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl',
            toolbar_sticky: true,
        });
    }

})

