
const testTask = {
    taskASsigned: 'Alex',
    taskDescription: 'Finish Math Homework'

}
export default function TaskList(){

    return(
     

<div>{formatTask(testTask, true)}</div>


    );
};
function formatTask(task, taskComplete){

    if(taskComplete === true){
       return(<li>The {task.taskDescription} is complete </li>);
    }
    return(<li>The {task.taskDescription} is not complete</li>);
    
}






