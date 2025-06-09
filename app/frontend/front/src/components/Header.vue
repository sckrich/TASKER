<script setup>
</script>
<template>
<div class="header">
        <div class="logo-block">
          <img class = "logo-img"src="../../public/Logo.png" alt="">
          <h1 class ="logo-text">TASKER</h1>
        </div>
        <div class="nav-block">
          <ul>
            <li>
              <router-link to="/"class = "link" href="#"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 10l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                <path d="M9 21v-6a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v6"/>
                
              </svg><a class = "text">Главная</a></router-link>
            </li>
            <li>
              
              <router-link to="groups"class = "link" href="#"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <circle cx="12" cy="6" r="3"/>
                <circle cx="6" cy="12" r="3"/>
                <circle cx="18" cy="12" r="3"/>
                <circle cx="12" cy="18" r="3"/>
                
                <path d="M12 9v6"/>
              </svg>
              <a class = "text">Группы</a></router-link>
            </li>
            <li>
              <router-link to="tasks"class = "link" href="#"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="3" y="5" width="18" height="16" rx="1"/>
                <line x1="7" y1="9" x2="17" y2="9"/>
                <line x1="7" y1="13" x2="17" y2="13"/>
                <line x1="7" y1="17" x2="13" y2="17"/>
              </svg><a class = "text">Задачи</a></router-link>
            </li>
            <li>
              <router-link to="profile"class = "link" href="#"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
              </svg><a class = "text">Профиль</a></router-link>
            </li>
          </ul>
        </div>
        <div class="registration-block">
          <router-link to="/registration" class = "reg-btn">Регистрация</router-link>
          <router-link to="/signin" class = "sgn-btn">Войти</router-link>
        </div>
      </div>
</template>
<style scoped>
.logo-img{
  width: 60px;
  object-fit: cover;
}
.header-line{
  opacity: 0.3;
  width: 90vw;
}
.sgn-btn:hover{
  outline: 1px solid rgb(156, 94, 255);
  transition: 0.2s ease;

}
.sgn-btn{
    color: rgb(156, 94, 255);
  text-decoration: none;
  font-family: "Geologica", sans-serif;
  padding: 6px;
  border-radius: 16px;
}
.reg-btn:hover{
  color: rgb(156, 94, 255);
  background-color: white;
  outline: 1px solid rgb(156, 94, 255);
  transition: 0.2s ease;
}
.reg-btn{
  text-decoration: none;

  font-family: "Geologica", sans-serif;
  color: white;
  padding: 6px;
  border-radius: 16px;
  background-color: rgb(156, 94, 255);
}
.logo-block{
  color: #343434;
  display: flex;
  align-items: center;
  font-family: "Geologica", sans-serif;
}
ul{
  display: flex;
  align-items: center;
  gap: 10px;
  list-style: none;
}
svg{
  margin-right: 4px;
}
li{
  display: flex;
  align-items: center;
}

.registration-block{
  display: flex;
  gap: 10px;
}
.link::after {
  
  width: 0;
  transition: 0.3s;
}
.link:hover:after {
  width: 100%;
  color: rgb(156, 94, 255);
}

.link {
  
  background:
    linear-gradient(currentColor 0 0) 0    100%/var(--d, 0) 2px no-repeat,
    linear-gradient(currentColor 0 0) 100% 100%/var(--d, 0) 2px no-repeat;
  transition:0.5s;
}
.link:hover {
  color: rgb(156, 94, 255);
  --d: 100%;
}

.link{
  position: relative;
  display: flex;
  padding-bottom: 6px;
  align-items: center;
  font-family: "Geologica", sans-serif;
  text-decoration: none;
  color: #292929;
}
.header{
  margin-top: 10px;
  height: 50px;
  width: 90vw;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
@media (max-width: 480px){
  .text{
    display: none;
  }
  .logo-text{
    display: none;
  }
  .registration-block{
    display: none;
  }
}
</style>