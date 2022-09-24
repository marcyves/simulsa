# Simul SA

Un projet perso à double tête qui me tiens à cœur depuis longtemps :

* Faire un jeu de simulation de gestion d'une entreprise
* Reprendre un vieux programme Basic publié dans le numéro 157 de Soft & Micro en février 1985


Dans un premier temps, c'est le jeu original qui est développé, et comme c'est de la vente de logiciel il y a quelques petites choses qui font date. Comme par exemple sur les choix disquette ou cassettte...

Dernier commentaire, pour l'instant c'est du Python, mais un jour peut-être une version Node.js permettrait de jouer à plusieurs.

Roadmap
-------

1. Transcrire le Basic Apple en Python (en cours)
2. Moderniser les textes
3. Implémenter de nouveaux modules pour améliorer la simulation
4. Faire une version multi joueurs

Règles du jeu original
----------------------

La date est initialisée et le joueur dispose d'un capital de 5000€. L'écran affiche les données du jour, c'est à dire quelques renseignements comme "le temps est pluvieux" ou "les logiciels de catégorie 7 et de qualité 1 se vendent mieux".

Le joueur peut effectuer jusqu'à quatre actions de base en fonction de sa situation commerciale et des renseignements affichés au début du jeu. Ces actions peuvent être choisies parmi quatre options.

 - La pemière concerne la fabrication : le joueur décide de créer un nouveau logiciel. Le programme demande alors les renseignements utiles (nom du logiciel, auteur, qualité de 1 à 5 et catégorie) qui lui serviront à agir sur les ventes. Il faut aussi entrer le support sur lequel sera commercialisé le programme (cassette ou disquette) et son prix, en tenant compte du cout de base indiqué par le programme.

 - La deuxième option, production, permet de lancer la fabrication en série d'un logiceil déjà développé. Le programme demande successivement le nom du logiciel et le nom de copies à produire. Le coût de l'opération est alors affiché.

 - La troisième option concerne la publicité, indispensable pour stimuler les ventes. Le programme demande le nom du logiciel à promouvoir et le choix des "supports" media. Ces renseignements entrés, il affiche le coût de la campagne de promotion.

 - La quatrième option du menu principal concerne la vente. Il s'agit de livrer les produits aux revendeurs, quitte à créer des points de vente si le joueur n'en possède aucun (c'est le cas au début du jeu). Pour créer un point de vente, il faut opter pour l'un des quinze noms disponibles. Comme vous le constaterez, la création d'un point de vente est relativement onéreuse et ce coût varie avec son efficacité. Plus elle est élevée et meilleures seront les ventes. Au début du jeu il faudra se contenter de petits points de vente et laisser s'accroitre son capital au fur et à mesure du développement, afin d'en acquérir des plus performants. Notez aussi qu'un point de vente ne peut diffuser simulanément plus de 5 articles.

 - La cinquième option permet de terminer la journée. Le programme affiche alors le bilan. Le revenu des ventes du jour est établi et les 90% de cette somme sont ajoutés au capital de la société. Le joueur ne peut jamais espérer réaliser une marge bénéficiaire supérieure à 30% sous peine de rendre le logiciel pratiquement invendable (cette règle simule les contraintes du marché d'une manière simple et efficace).

 Si le capital final, c'est-à-dire après le bilan de fin de journée, s'élève à moins de 100€, c'est la faillite et il ne reste qu'à rejouer. Si par contre il dépasse 1 000 000€ ou si la société commercialise plus de 45 logiciels, le joueur est considéré comme "maitre du marché".
