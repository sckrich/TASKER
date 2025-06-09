<script setup>
</script>
<template>
    <div class="footer">
        <div class="footer-info">
            <p>TASKER — это мощное веб-приложение для управления задачами, которое помогает вам организовать свою работу и повысить продуктивность. Создавайте, отслеживайте и делитесь задачами с командой в удобном интерфейсе.</p>
            <h3>Контактная информация:</h3>
            <div class="btns">
              <a href="#">Вконтакте</a>
              <a href="#">Телеграмм</a>
              <a href="#">Почта</a>
            </div>
        </div>
        <div class="footer-bottom">
        <small>© 2025 TASKER. Все права защищены.</small>
    </div>
      </div>
</template>
<style scoped>
.btns{
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
}
.footer-bottom{
  color: white;
  margin-bottom: 10px;
}
.footer-btns{
  color: rgb(156, 94, 255);
  margin-left: auto;
  margin-right: auto;
}
a:hover{
  background-color: rgb(156, 94, 255);
  color: white;
  outline: 1px solid white;
  transition: 0.2s ease;
}
ul{
  list-style: none;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  gap: 8px;
}
a{
  text-decoration: none;
  background-color: white;
  padding: 6px;
  border-radius: 8px;
}
.footer{
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Geologica", sans-serif;
  background-color: rgb(156, 94, 255);
}
.footer-info{
  color: white;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 90vw;
  text-align: center;
}
</style>