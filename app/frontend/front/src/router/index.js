import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Tasks from '@/views/Tasks.vue'
import Profile from '@/views/Profile.vue'
import Groups from '@/views/Groups.vue'
import Registration from '@/views/Registration.vue'
import SignIn from '@/views/SignIn.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/tasks',
      name: "tasks",
      component: Tasks,
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
    {
      path: "/groups",
      name: "groups",
      component: Groups,
    },
    {
      path: '/registration',
      name: "registration",
      component: Registration
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignIn
    }
  ],
})

export default router
