const today = new Date();
const testTask = {
    taskName: 'Do Hoemwork',
    taskDescription: 'Finish Math Homework'

}
export default function taskList(){

    return(
     
<></>
    );
};

//Returns the day of the week that is today.
function formatDate(date){
    return new Intl.DateTimeFormat(
        'en-us',
        {weekday:'long'}
    ).format(date)
}






