import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Login from "../views/Login.vue";
// import register from '../views/Register.vue'
import store from "../store/index";

function isAdmin(to, from, next) {
  const userRole = window.localStorage.getItem("userRole");
  if (userRole === "admin") {
    next(); // Allow access for admin
    console.log("User Role:", userRole); // Log the user role
  } else {
    console.log("Redirecting to unauthorized"); // Log the redirection
    next("/unauthorized"); // Redirect other users to an unauthorized page
  }
}

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/register",
    name: "register",
    component: () =>
      import(/* webpackChunkName: "register" */ "../views/Register.vue"),
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: () =>
      import(/* webpackChunkName: "Dashboard" */ "../views/Dashboard.vue"),
    beforeEnter: isAdmin,
  },
  {
    path: "/createvenue",
    name: "createvenue",
    component: () =>
      import(/* webpackChunkName: "createvenue" */ "../views/createVenue.vue"),
    beforeEnter: isAdmin,
  },
  {
    path: "/modifyvenue/:venueId",
    name: "modifyvenue",
    component: () =>
      import(/* webpackChunkName: "modifyvenue" */ "../views/modifyVenue.vue"),
    beforeEnter: isAdmin,
  },
  {
    path: "/createshow/:venueId",
    name: "createshow",
    component: () =>
      import(/* webpackChunkName: "createshow" */ "../views/createShow.vue"),
    beforeEnter: isAdmin,
  },
  {
    path: "/venue/:venueId/show/:showId",
    name: "modifyshow",
    component: () =>
      import(/* webpackChunkName: "modifyshow" */ "../views/modifyShow.vue"),
    beforeEnter: isAdmin,
  },
  {
    path: "/venue/:venueId/show/:showId/delete",
    name: "deleteshow",
    component: () =>
      import(/* webpackChunkName: "deleteshow" */ "../views/deleteShow.vue"),
    beforeEnter: isAdmin,
  },
  {
    path: "/venue/:venueId/delete",
    name: "deletevenue",
    component: () =>
      import(/* webpackChunkName: "deletevenue" */ "../views/deleteVenue.vue"),
    beforeEnter: isAdmin,
  },
  // {
  //   path: "/venue/:venueId",
  //   name: "venue",
  //   component: () =>
  //     import(/* webpackChunkName: "venue" */ "../views/Venue.vue"),
  // },
  // {
  //   path: "/show/:showId",
  //   name: "show",
  //   component: () =>
  //     import(/* webpackChunkName: "show" */ "../views/Show.vue"),
  // },
  {
    path: "/unauthorized",
    name: "unauthorized",
    component: () =>
      import(/* webpackChunkName: "unauthorized" */ "../views/Unauthorized.vue"),
  },
  // {
  //   path: "/:catchAll(.*)",
  //   name: "notfound",
  //   component: () =>
  //     import(/* webpackChunkName: "notfound" */ "../views/NotFound.vue"),
  // },
  //user dashboard
  {
    path: "/home",
    name: "userdashboard",
    component: () => import("../views/userDashboard.vue"),
  },
  {
    path: "/booking/:showId",
    name: "userbooking",
    component: () => import("../views/userBooking.vue"),
  },
  {
    path: "/search",
    name: "search",
    component: () => import("../views/searchPage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
