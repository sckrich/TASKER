<script setup>
import axios from 'axios';
import { ref } from 'vue';

import { errorMessages } from 'vue/compiler-sfc';
const email = ref('')
const password = ref('')
const username = ref('')
const fname = ref('')
const lname = ref('')
const mname = ref('')
const birth_date = ref('')

const submitlogin = async () =>{
    try{
    const response = await axios.post('http://localhost:9091/api/SignUp/', {
        "username": username.value,
        "user_password": password.value,
        "first_name": fname.value,
        "last_name": lname.value,
        "middle_name": mname.value,
        "user_email": email.value,
        "user_birthdate": birth_date.value 
    })
    }
    catch(error){
        console.error("Error : - ", error)
    }
}
function show(){
    console.log(username.value, password.value, fname.value, lname.value, mname.value, email.value, birth_date.value )
}
</script>
<template>
<div class="form">
    <div class="form-wrapper">
    <form @submit.prevent="submitlogin">
        <div class="email">
            <h3>Логин:</h3>
            <input v-model="username" type="text" placeholder="Логин">
        </div>
        <div class="email">
            <h3>Ваше имя:</h3>
            <input v-model="fname" type="text" placeholder="Имя">
        </div>
        <div class="email">
            <h3>Ваша фамилия:</h3> 
            <input v-model="lname" type="text" placeholder="Фамилия">
        </div>
        <div class="email">
            <h3>Ваше отчество (при наличии):</h3>
            <input v-model="mname" type="text" placeholder="Отчество">
        </div>
        <div class="email">
        <h3>Дата рождения:</h3>
            <input v-model="birth_date" type="date" placeholder="Дата рождения">
        </div>
        <div class="email">
            <h3>Ваш E-mail</h3>
            <input v-model="email" type="text" placeholder="Почта">
        </div>
        <div class="pass">
        <h3>Пароль:</h3>
            <input v-model="password" type="password" placeholder="Пароль">
        </div>
        <button @click="show()">Show</button>
        <button type="submit">Войти</button>
        <div class="reg">
            <p class = "reg-text">Уже есть аккаунт? - </p>
            <router-link to="/registration">Войдите</router-link>
        </div>

    </form>
    <div class="signin-with">
        <p class = "gray">Или войдите с помощью</p>
        <div class="btns">
        <button class ="sign-btn">Яндекс</button>
        <button class="sign-btn">ВКонтакте</button>
        </div>
    </div>
    </div>
  
</div>
</template>
<style scoped>
.reg-text{
    margin: 0;
    margin-top: 10px;
}
.signin-with{
    display: flex;
    flex-direction: column;
    align-items: center;
    border-top: 1px solid rgb(156, 94, 255);
    margin-top: 20px;
}
.gray{
    padding: 0;
    margin: 0;
    margin-top: 8px;
    color: gray;
}
input:focus{
  outline: 1px solid rgb(156, 94, 255);
}
input{
    min-width: 300px;
  font-size: 16px;
  padding: 8px;
  width: 250px;
  font-family: "Geologica", sans-serif;
  border-radius: 8px;
  border: 1px solid gray;
}
.form{
    display: flex;
    margin-bottom: 30px;
    margin-top: 20px;
}
button:active{
  transform: scale(0.95);
}
button{
    min-width: 200px;
    margin-top: 10px;
  padding: 8px;
  background-color: rgb(156, 94, 255);
  color: white;
  font-size: 18px;
  border-radius: 8px;
  margin-left: 8px;
  border: none;
}
button:hover{
  cursor: pointer;
  transition: 0.3s ease;
  outline: 1px solid rgb(156, 94, 255);;
  background-color: white;
  color: rgb(156, 94, 255);
}
a:hover{
    color: rgb(113, 69, 184);
}
.reg{
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
}
form{
    display: flex;
    flex-direction: column;
    align-items: center;
}
a{
    text-decoration: none;
    margin-top: 4px;
}
.form-wrapper{
    border: 1px solid rgb(156, 94, 255);
    border-radius: 16px;
    padding: 10px;
    margin-top: auto;
    margin-bottom: auto;
    font-family: "Geologica", sans-serif;
    color: #343434;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
}
</style>