import { createRouter, createWebHistory } from 'vue-router'
import Search from '../views/Search.vue'
import HomeView from '../views/HomeView.vue'
import Catagory from '../views/Catagory.vue'
import Product from '../views/Product.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import Account from '../views/Account.vue'
import store from '@/store'

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
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/account',
    name: 'Account',
    component: Account,
    meta: {
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  //if require login and not authenticated
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    //redirect path to login
    next({ name: 'Login', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
