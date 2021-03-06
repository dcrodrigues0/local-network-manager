import Vue from 'vue'
import VueRouter from 'vue-router'

import Main from '@/components/Main.vue'
import View1 from '@/components/view1.vue'

Vue.use(VueRouter)


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Main
    },
    {
        path: '/view1',
        name: 'View1',
        component: View1
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router