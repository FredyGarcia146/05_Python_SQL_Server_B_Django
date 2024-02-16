//You may use vanilla JS, I just chose jquery

// Comando que nos ayuda a iniciar funciones cuando arranca el index.html
document.addEventListener("DOMContentLoaded",init)
constUrl = 'http://127.0.0.1:8000/api/'

function init(){
    search()
}
// async espera que termine las funcion por funcion para ir al siguiente
async function search(){
    var url = constUrl + 'postulant'
    var response = await fetch(
            url,
            {
                "method":'GET',
                "headers":{
                    "Content-Type":'application/json'
                }
            }
        )
    var resultado = await response.json()
    // window.alert(resultado)         
    var html=''
    var row =''
    for (postulant of resultado){
        row=`
            <tr>
            <td>${postulant.Id}</th>
            <td>${postulant.Name }</td>
            <td>${postulant.First_Name }</td>
            <td>${postulant.Second_Name }</td>
            <td>${postulant.Age }</td>
            <td>${postulant.Profession }</td>
            <td>${postulant.Actual_State }</td>
            <td>
                <button class="myButtonAceptar" onclick="addReasonAccept(${postulant.Id})">Aceptar</button>
                <button class="myButtonRechazar"onclick="addReasonDenied(${postulant.Id})">Rechazar</button>
            </td>
            <td>
                <button class="myButtonModificar"   onclick="modifyPostulantDetails(${postulant.Id})">Modificar</button>
                <button class="myButtonEliminar"    onclick="Delete(${postulant.Id})">Eliminar</button>
            </td>
            </tr>
        `
        html=html + row
    }

    document.querySelector('#postulants > tbody').outerHTML =html
}


async function Delete(Id){
    var option = confirm('Desea Eliminar al Usuario : ' + Id)
    if(option == true){
        var url = constUrl + 'postulant/' + Id 
        var response = await fetch(
                url,
                {
                    "method":'DELETE',
                    "headers":{
                        "Content-Type":'application/json'
                    }
                }
            )
        window.location.reload();
    }
}

async function AddPostulant(){

    var data={
            "Name":document.getElementById('txtName').value,
            "First_Name":document.getElementById('txtFirstLastName').value,
            "Second_Name":document.getElementById('txtSecondLastName').value,
            "Age":document.getElementById('txtAge').value,
            "Profession":document.getElementById('txtOcupation').value
            // "Actual_State":"Sin Definir"
            // "Date_Registration":"2022-09-13",
            // "Date_Modificate":"2022-09-13 06:46:26.118480"
    }
    var url = constUrl + 'postulant/'
    var response = await fetch(
            url,
            {
                "method":'POST',
                "body":JSON.stringify(data),
                "headers":{
                    "Content-Type":'application/json'
                }
            }
        )
    window.location.reload();
}
function addPostulantDetails(){
    htmlModal = document.getElementById("modal-Agregar");
    htmlModal.setAttribute("class","modale opened");

};


function modifyPostulantDetails(Id){
    modifyPostulant(Id)
};

async function modifyPostulant(Id){
    htmlModal = document.getElementById("modal-Modificar");
    htmlModal.setAttribute("class","modale opened");

    var url = constUrl + 'postulant/' + Id
    var response = await fetch(
            url,
            {
                "method":'GET',
                "headers":{
                    "Content-Type":'application/json'
                }
            }
        )
    var resultado = await response.json()
    // window.alert(resultado)       
    var html=''
    var row =''
    // window.alert(row) 
    // for (postulant of resultado){
    //     row=`
    //     <div id ='DetailsPostulant'class="modal-body">
    //         <b id ='CodePostulant'>${postulant.Id}</b><br>
    //         <input id='txtNameModify' type="text" name="u" value="${postulant.Name}" size="20" /><br>
    //         <input id='txtFirstLastNameModify' type="text" name="u" value="${postulant.First_Name}" size="20" /><br>
    //         <input id='txtSecondLastNameModify' type="text" name="u" value="${postulant.Second_Name}" size="20" /><br>
    //         <input id='txtAgeModify' type="text" name="u" value="${postulant.Age}" size="20" /><br>
    //         <input id='txtOcupationModify' type="text" name="u" value="${postulant.Profession}" size="20" /><br>
    //     </div>
    //     `
    //     window.alert(postulant)
    //     html=html + row
    // }
    // window.alert(html)
    row=`
        <div id ='DetailsPostulant'class="modal-body">
            <b id ='CodePostulant'>${resultado.Id}</b><br>
            <input id='txtNameModify' type="text" name="u" value="${resultado.Name}" size="20" /><br>
            <input id='txtFirstLastNameModify' type="text" name="u" value="${resultado.First_Name}" size="20" /><br>
            <input id='txtSecondLastNameModify' type="text" name="u" value="${resultado.Second_Name}" size="20" /><br>
            <input id='txtAgeModify' type="text" name="u" value="${resultado.Age}" size="20" /><br>
            <input id='txtOcupationModify' type="text" name="u" value="${resultado.Profession}" size="20" /><br>
        </div>
        `
        // window.alert(row)
    document.querySelector('#DetailsPostulant').outerHTML =row
}

async function ModifyPostulantBase(){
    var option = confirm('Desea Modificar al Usuario : ' + document.getElementById('CodePostulant').innerHTML)
    var id = document.getElementById('CodePostulant').innerHTML
    if (option == true){
        var data={
                // "Id":document.getElementById('CodePostulant').innerHTML,
                "Name":document.getElementById('txtNameModify').value,
                "First_Name":document.getElementById('txtFirstLastNameModify').value,
                "Second_Name":document.getElementById('txtSecondLastNameModify').value,
                "Age":document.getElementById('txtAgeModify').value,
                "Profession":document.getElementById('txtOcupationModify').value
        }
        var url = constUrl + 'postulant/' +id
        var response = await fetch(
                url,
                {
                    "method":'PUT',
                    "body":JSON.stringify(data),
                    "headers":{
                        "Content-Type":'application/json'
                    }
                }
            )
        window.location.reload();
    }
}


function addReasonAccept(Id){
    htmlModal = document.getElementById("reason");
    htmlModal.setAttribute("class","modale opened");
    action = 'Accept'

    html = `<b id ='CodePostulantReason'>${Id}</b>`
    document.querySelector('#CodePostulantReason').outerHTML =html
    html = `<b id ='reasonAplication'>${action}</b>`
    document.querySelector('#reasonAplication').outerHTML =html
};



function addReasonDenied(Id){
    htmlModal = document.getElementById("reason");
    htmlModal.setAttribute("class","modale opened");
    action = 'Denied'

    html = `<b id ='CodePostulantReason'>${Id}</b>`
    document.querySelector('#CodePostulantReason').outerHTML =html
    html = `<b id ='reasonAplication'>${action}</b>`
    document.querySelector('#reasonAplication').outerHTML =html

};

async function changeStatePostulation(){
    typeChangeState = document.getElementById('reasonAplication').innerHTML
    var id = document.getElementById('CodePostulantReason').innerHTML
    var option = confirm('You want to '+typeChangeState+' the user : ' + id)
    if (option == true){
        var data={
                // "Id":document.getElementById('CodePostulantReason').innerHTML,
                "Reason":document.getElementById('bodyReason').value,
                "State":typeChangeState
        }
        var url = constUrl + 'postulant/' + id
        var response = await fetch(
                url,
                {
                    "method":'PATCH',
                    "body":JSON.stringify(data),
                    "headers":{
                        "Content-Type":'application/json'
                    }
                }
            )
        window.location.reload();
    }
}





function closeModal(){
    htmlModal = document.getElementById("modal-Agregar");
    htmlModal.setAttribute("class","modale");
    htmlModal = document.getElementById("modal-Modificar");
    htmlModal.setAttribute("class","modale");
    htmlModal = document.getElementById("reason");
    htmlModal.setAttribute("class","modale");
};