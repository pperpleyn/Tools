function sortData() {
    fetch('/sort-files', { method: 'POST' })
        .then(() => {
            // Force browser to display the redirected/refreshed page
            window.location.reload();
        })
        .catch(error => console.error('Error sorting files:', error));
}

function refreshList() {
    window.location.href = '/refresh-1'
}

document.querySelectorAll('.clickable-item').forEach(item => {

    item.addEventListener('click', function() {

        const path = this.getAttribute('data-path');

        

        // Send fetch request directly inside event listener

        fetch('/process-file', {

            method: 'POST',

            headers: {

                'Content-Type': 'application/json'

            },

            body: JSON.stringify({ item: path }) // Sends key matching Flask's data.get('item')

        })

        .then(response => response.json())

        .then(data => {

            console.log('Success:', data);

        })

        .catch(error => console.error('Error:', error));

    });

});
