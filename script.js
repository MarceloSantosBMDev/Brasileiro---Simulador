
// Função para baixar o arquivo
function baixarArquivo(url, nomeArquivo) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro ao baixar o arquivo: ${response.statusText}`);
            }
            return response.blob(); // Converte a resposta em um Blob
        })
        .then(blob => {
            // Cria um link temporário para o Blob
            const urlBlob = window.URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = urlBlob;
            link.download = nomeArquivo; // Define o nome do arquivo para download
            document.body.appendChild(link);
            link.click(); // Simula o clique no link para iniciar o download
            document.body.removeChild(link); // Remove o link do DOM
            window.URL.revokeObjectURL(urlBlob); // Libera o objeto URL
        })
        .catch(error => console.error("Erro ao baixar o arquivo:", error));
}

// Adiciona eventos de clique aos botões de download
document.querySelectorAll('.download-button').forEach((botao) => {
    botao.addEventListener('click', () => {
        const nomeArquivo = botao.getAttribute('data-file'); // Obtém o nome do arquivo
        const githubRawUrl = `https://raw.githubusercontent.com/2pacdevv/Brasileiro---Simulador/main/${nomeArquivo}`; // URL do arquivo no GitHub
        baixarArquivo(githubRawUrl, nomeArquivo); // Inicia o download
    });
});