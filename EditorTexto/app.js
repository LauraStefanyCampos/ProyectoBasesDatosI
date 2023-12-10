const editorUpdate = () => {
    const htmlText = document.querySelector('#htmlText');
    const cssText = document.querySelector('#cssText');
    const jsText = document.querySelector('#jsText');
    const textoView = document.querySelector('#textoVista');

    textoView.srcdoc = `
        <html>
        <head>
            <style>${cssText.value}</style>
        </head>
        <body>${htmlText.value}<script>${jsText.value}</script></body>
        </html>
    `;

    // Aplicar resaltado de sintaxis con Prism
    Prism.highlightAll();
}



const saveContent = () => {
    const htmlText = document.querySelector('#htmlText');
    const cssText = document.querySelector('#cssText'); // Corregido el ID
    const jsText = document.querySelector('#jsText'); // Corregido el ID
    const textoView = document.querySelector('#textoVista');

    const combinedContent = `
        <html>
        <head>
            <style>${cssText.value}</style>
        </head>
        <body>${htmlText.value}<script>${jsText.value}</script></body>
        </html>
    `;

    const blob = new Blob([combinedContent], { type: 'text/html' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = 'output.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
