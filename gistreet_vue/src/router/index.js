import { createRouter, createWebHistory } from 'vue-router'
import Search from '../views/Search.vue'
import HomeView from '../views/HomeView.vue'
import Catagory from '../views/Catagory.vue'
import Product from '../views/Product.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/:catagory_slug/:product_slug/',
    name: 'Product',
    component: Product
  },
  {
    path: '/:catagory_slug',
    name: 'Catagory',
    component: Catagory
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
