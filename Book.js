class Workout {
    constructor(time,date,type){
        this.time = time
        this.date = date
        this.type = type
    }
    getTime() {
        return time
    }
    getDate() {
        return date
    }
    getType() {
        return type
    }

    getInfo(){
        return `<i class="fa-regular fa-calendar-days"></i> Date: ${this.date}, <i class="fa-solid fa-clock"></i> Time: ${this.time}, <i class="fa-solid fa-trophy"></i> Type: ${this.type}`
    }
}

const btn = document.querySelector("#Book");
const Workouts = [];
const Workouts_list = document.querySelector("#booked-workouts-list")

btn.addEventListener("click", (e) => {
    e.preventDefault()
    const training_time = document.querySelector("#training-time").value
    const training_date = document.querySelector("#training-date").value
    const training_type = document.querySelector("#training-type").value

    if (training_date != ""){
        const title = document.querySelector("#ul-title")
        title.textContent = "Your upcoming workouts"
        Workouts_list.innerHTML = ""

        console.log(training_time)
        console.log(training_date)
        console.log(training_type)
        Workouts.push(new Workout(training_time,training_date,training_type))


        Workouts.forEach(function(Workout) {
            Workouts_list.innerHTML += "<li><h2>" + Workout.getInfo() + "</h2></li>"
        });
    } else {
        const date_select = document.querySelector("#training-date")
        date_select.style.border = " 2px solid red"
        window.alert("Please enter a date for your workout")
    }
});



