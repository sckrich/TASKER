<script setup>
import { ref } from 'vue';
const email = ref('');
</script>

<template>
  <main>
    <div class="info-sign-block">
      <div class="information">
        <h1 class = "title">Приветствуем вас в TASKER</h1>
        <p class = title-text>Добро пожаловать на наш сайт менеджмента задач! Наша платформа создана для того, чтобы помочь вам организовать свои задачи и проекты максимально эффективно.</p>
        <div class="email-block">
          <div class="email">
            <input v-model="email" type="text" placeholder="Email">
            <button type="button">Войти</button>
          </div>
          <div class="license">
            <p class="gray-title">Отправляя свою почту, я подтверждаю</p>
            <a class = "license-link"href="/license">политику использования TASKER</a>
          </div>
          <div class="video">
            <p class="title">Смотреть видео</p>
            <button type="button" class = "video-btn">Смотреть</button>
          </div>
        </div>
      </div>
      <div class="image">
        <img src="../../public/programmer.png" alt="" class="body-img">
      </div>
    </div>
    <div class="third-block">
      <div class="img">
        <img class = "main-img"src="../../public/main-img.jpg" alt="">
      </div>
      <div class="info-text">
        <h1 class="title">Преимущества использования TASKER</h1>
        <p class="title-text">TASKER предоставляет интуитивно понятный и простой в использовании интерфейс, который позволяет пользователям легко организовывать свои задачи и проекты. Это делает его доступным как для индивидуальных пользователей, так и для команд.</p>
        <p class="title-text">Пользователи могут создавать и настраивать доски, списки и карточки в соответствии с их уникальными потребностями. Это позволяет адаптировать приложение под различные рабочие процессы и стили управления проектами.</p>
        <p class="title-text">TASKER предоставляет инструменты для отслеживания прогресса и производительности, что позволяет пользователям анализировать свою работу и вносить необходимые изменения для повышения эффективности.</p>
      </div>
      
    </div>
    <div class="sec-block">
      <div class="email-end-block">
      <h1 class = "title">Начните работать в TASKER</h1>
        <div class="email">
            <input v-model="email" type="text" placeholder="Email">
            <button type="button">Войти</button>
          </div>
          <div class="license">
            <p class="gray-title">Отправляя свою почту, я подтверждаю</p>
            <a class = "license-link"href="/license">политику использования TASKER</a>
          </div>
        </div>
    </div>
  </main>
</template>
<style scoped>
.main-img{
  width: 100%;
  border-radius: 32px;
}
.info-text{
  margin-left: 20px;
}
.third-block{
  display: grid;
  grid-template-columns: auto auto;
  font-family: "Geologica", sans-serif;
  width: 80vw;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 20px;
  background-color: rgb(156, 94, 255);
  color: white;
  border-radius: 40px;
  padding: 8px;
}
.sec-block{
  background-color: rgb(238, 238, 238);
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-top: auto;
  margin-bottom: auto;
  font-family: "Geologica", sans-serif;
  color: #343434;
}
.video-btn:hover{
  cursor: pointer;
  transition: 0.3s ease;
  outline: 1px solid rgb(156, 94, 255);;
  background-color: white;
  color: rgb(156, 94, 255);
}
.video-btn{
  padding: 10px;
  background-color: rgb(156, 94, 255);
  color: white;
  font-size: 18px;
  border-radius: 8px;
  margin-left: 8px;
  border: none;
}
.video{
  display: flex;
  align-items: center;
}
button:active{
  transform: scale(0.95);
}
button{
  padding: 10px;
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
.gray-title{
  color: gray;
}
.email{
  display: flex;
  align-items: center;
}
.license-link::after {
  
  width: 0;
  transition: 0.3s;
}
.license-link:hover:after {
  width: 100%;
  color: rgb(156, 94, 255);
}
.license-link:hover {
  color: rgb(156, 94, 255);
  --d: 100%;
}
.license-link{
  text-decoration: none;
  color: rgb(156, 94, 255);
  background:
    linear-gradient(currentColor 0 0) 0    100%/var(--d, 0) 2px no-repeat,
    linear-gradient(currentColor 0 0) 100% 100%/var(--d, 0) 2px no-repeat;
  transition:0.5s;
}
input:focus{
  outline: 1px solid rgb(156, 94, 255);
}
input{
  font-size: 18px;
  padding: 8px;
  width: 250px;
  font-family: "Geologica", sans-serif;
  border-radius: 8px;
  border: 1px solid gray;
}
.license{
  display: flex;
  align-items: center;
  gap: 8px;
}
.info-sign-block{
  display: grid;
  grid-template-columns: auto auto;
  width: 80vw;
  margin-left: auto;
  margin-right: auto;
}
.information{
  display: flex;
  flex-direction: column;
  margin-top: auto;
  margin-bottom: auto;
  font-family: "Geologica", sans-serif;
  color: #343434;
}

.body-img{
  width: 100%;
}
@media (max-width: 480px){
  .info-sign-block{
  display: flex;
  flex-direction: column;
  width: 80vw;
  margin-left: auto;
  margin-right: auto;
}
.third-block{
  display: flex;
  flex-direction: column;
}
.email-end-block{
  margin-left: 4%;
}
.license{
  display: contents;
}
.info-text{
  margin-left: 5px;
}
}
</style>