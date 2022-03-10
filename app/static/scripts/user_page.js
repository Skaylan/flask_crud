form = document.querySelector('#task-form');

const submitFormDelete = () => {
    const value = confirm('Are you sure you want to delete this task?');
    
    if(value === true) {
        form.submit();
    }else {
        //
    }
}