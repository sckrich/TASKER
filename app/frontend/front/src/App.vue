<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div class="app">
    <div class="wrapper">
      <Header></Header>
      <RouterView></RouterView>
      <Footer></Footer>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Geologica:wght@100..900&display=swap');
.app{
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  overflow-x: hidden;
}
.wrapper{
  overflow-x: hidden;
}

</style>
