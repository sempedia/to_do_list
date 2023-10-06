

// Add New Task Modal
function showAddTaskModal() {
    $('#addTaskModal').modal('show');
}

// Edit Task Modal
function showEditTaskModal(taskId) {
    $(`#editTaskModal${taskId}`).modal('show');
}


  // Your JavaScript code for showing confirmation popups
function showConfirmationPopup(event) {
    return confirm('Are you sure you want to delete this task?');
}

// Handle the click event on the "Edit" button using jQuery
$(function () {
    $('.btn-outline-primary').on('click', function () {
    var targetModalId = $(this).data('bs-target');
    $(targetModalId).modal('show');
    });
});
