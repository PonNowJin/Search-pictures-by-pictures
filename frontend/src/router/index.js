import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomePage.vue';
import Results from '../views/SearchResults.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/results',
    name: 'Results',
    component: Results
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
