<template>
  <v-app id="inspire">
    <v-system-bar app>
      <v-spacer></v-spacer>
        <!--
      <v-icon>mdi-square</v-icon>

      <v-icon>mdi-circle</v-icon>
s
      <v-icon>mdi-triangle</v-icon>
      -->
    </v-system-bar>

    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-sheet
        color="grey lighten-4"
        class="pa-4"
      >
        <v-avatar
          class="mb-4"
          color="grey darken-1"
          size="64"
        ></v-avatar>

        <div>Aktuelle Gesetzgebungsverfahren</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list>
        <v-list-item
          v-for="[icon, text] in links"
          :key="icon"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-container
        class="py-8 px-6"
        fluid >
      <p>Voila</p>
        <Gesetze></Gesetze>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Gesetze from './components/Gesetze';


  export default {
    data: () => ({
      cards: ['in parlamentarischer Beratung', 'Beratung abgeschlossen'],
      drawer: null,
      // links: [
        //['mdi-inbox-arrow-down', 'Inbox'],
        //['mdi-send', 'Send'],
        //['mdi-delete', 'Trash'],
        //['mdi-alert-octagon', 'Spam'],
     // ],
      testgesetze: [
                {
                        id: 1,
                        name: "EGovG",
                        status : "beschlossen",
                },
                {
                         id: 2,
                         name: "PAG",
                         status: "eingebracht",
                        
                },
      ],
    }),
    components: {
            Gesetze,
    },
  }

  
</script>