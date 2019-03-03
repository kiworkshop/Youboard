import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/channel',
            name: 'channel',
            component: () => import('@/views/Channel.vue')
        },
        {
            path: '/youtuber',
            name: 'youtuber',
            component: () => import('@/views/Youtuber.vue')
        }
    ]
})