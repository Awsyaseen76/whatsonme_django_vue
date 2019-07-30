import Vue from "vue";
import Router from "vue-router";
import AuthList from "./components/auth_list.vue";
import AddAuth from "./components/add_auth.vue";
import SearchAuths from "./components/search_auth.vue";
import AuthDetails from "./components/auth_details.vue";

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "AuthList",
            alias: "/Auths",
            component: AuthList,
            children: [
                {
                    path: "/Auths/:id",
                    name: "auth_details",
                    component: AuthDetails,
                    props: true
                }
            ]
        },
        {
            path: "/add",
            name: "add",
            component: AddAuth
        },
        {
            path: "/search",
            name: "search",
            component: SearchAuths
        }
    ]
});