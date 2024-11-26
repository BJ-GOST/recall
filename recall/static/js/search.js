let originalNotes = []; // To store original notes loaded initially

// Function to filter and display notes based on search query
function searchNotes() {
    const query = document.getElementById('searchInput').value.toLowerCase().trim(); // Get search query

    // Clear previous search results
    const searchResultsDiv = document.getElementById('searchResults');
    searchResultsDiv.innerHTML = '';

    // If query is empty, display original notes
    if (query === '') {
        displayNotes(originalNotes);
        return;
    }

    // Filter notes based on the query (searching by title or tags)
    const filteredNotes = originalNotes.filter(note => {
        return note.title.toLowerCase().includes(query) || note.tags.some(tag => tag.name.toLowerCase().includes(query));
    });

    // If no filtered results, show "No notes found"
    if (filteredNotes.length === 0) {
        const noResultsElement = document.createElement('p');
        noResultsElement.textContent = 'No notes found';
        searchResultsDiv.appendChild(noResultsElement);
    } else {
        // Display the filtered notes
        displayNotes(filteredNotes);
    }
}

// Function to display a list of notes
function displayNotes(notes) {
    const searchResultsDiv = document.getElementById('searchResults');
    searchResultsDiv.innerHTML = ''; // Clear previous results

    notes.forEach(result => {
        const noteElement = document.createElement('div');
        noteElement.className = 'flex-none min-h-16 md:h-16 w-full p-2 flex flex-col md:flex-row items-center bg-teal rounded-md space-y-2 md:space-y-0';

        const titleDiv = document.createElement('div');
        titleDiv.className = 'w-full md:w-1/2 h-8 md:h-full flex flex-row items-center text-base text-white';
        const titleSpan = document.createElement('span');
        titleSpan.textContent = result.title;
        titleDiv.appendChild(titleSpan);

        const tagsDiv = document.createElement('div');
        tagsDiv.className = 'w-full md:w-1/2 h-8 md:h-full flex flex-row items-center justify-start space-x-2';

        // Check if tags exist and loop through to create tags div
        if (Array.isArray(result.tags)) {
            result.tags.slice(0, 4).forEach(tag => {
                const tagDiv = document.createElement('div');
                tagDiv.className = 'w-16 h-1/2 md:h-full bg-yellow text-black text-xs rounded-md flex flex-col items-center justify-around';
                tagDiv.textContent = tag.name.length > 7 ? tag.name.substring(0, 7) + '...' : tag.name; // Truncate tag name to 7 chars
                tagsDiv.appendChild(tagDiv);
            });
        }

        const actionsDiv = document.createElement('div');
        actionsDiv.className = 'w-full md:w-1/2 h-8 md:h-full flex flex-row items-center justify-start space-x-2';

        const viewButton = document.createElement('a');
        viewButton.className = 'w-20 md:w-24 h-full md:h-3/4 p-2 bg-white text-black text-sm rounded-md text-center';
        viewButton.href = `/api/note-detail/${result.id}`;
        viewButton.textContent = 'View';
        actionsDiv.appendChild(viewButton);

        const updateButton = document.createElement('a');
        updateButton.className = 'w-20 md:w-24 h-full md:h-3/4 p-2 bg-white text-black text-sm rounded-md text-center';
        updateButton.href = `/api/update-note/${result.id}`;
        updateButton.textContent = 'Update';
        actionsDiv.appendChild(updateButton);

        noteElement.appendChild(titleDiv);
        noteElement.appendChild(tagsDiv);
        noteElement.appendChild(actionsDiv);

        searchResultsDiv.appendChild(noteElement);
    });
}


document.addEventListener('DOMContentLoaded', () => {
    // Fetch original notes (adjust this endpoint to your actual one)
    fetch('/api/get-notes/')
        .then(response => response.json())
        .then(data => {
            originalNotes = data.results; // Store the original notes in the variable

            // Check if there are any notes
            if (originalNotes.length === 0) {
                // No notes found, display a message
                const searchResultsDiv = document.getElementById('searchResults');
                const noNotesElement = document.createElement('p');
                noNotesElement.textContent = 'No notes yet'; // Message to display when there are no notes
                searchResultsDiv.appendChild(noNotesElement);
            } else {
                // There are notes, display them
                displayNotes(originalNotes);  // Display them initially
            }
        })
        .catch(error => {
            console.error('Error fetching notes:', error);
            // Handle the error (optional)
            const searchResultsDiv = document.getElementById('searchResults');
            const errorElement = document.createElement('p');
            errorElement.textContent = 'An error occurred while fetching notes.';
            searchResultsDiv.appendChild(errorElement);
        });
});

