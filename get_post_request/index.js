let p =  fetch ("https://reqres.in/api/users/2")
p.then ((value) => {
    console.log (value.status)
    console.log (value.ok)
    return value.json()
}).then ((value) => {
    console.log (value)
})

const createToDo = async (data) => {
    let options = {
        method : "POST",
        headers : {
            "Content-type" : "application/json"
        },
        body : JSON.stringify (data),
    }
    let p = await fetch ("https://reqres.in/api/users/2", options)
    let response = await p.json()
    return response
}

const mainFunc = async () => {
    let todo = {
        title : "Something",
        body : "some",
        userId : 11,
    }
    let todor = await createToDo (todo)
    console.log (todor)
}

mainFunc ()