"""
Configuration

Author: Tong
Time: 24-06-2021
"""
user_id = "bahuia"  # github id
author_info = "Yongrui Chen"  # used in introduction
personal_link = ""  # used in introduction
repo_name = "Awesome_Continual_Learning"  # repository name
branch_name = "master"  # branch name
your_research_topic = "CL"  # used for dictionary name
your_research_topic_full_name = "Continual-Learning"  # used for title
bib_link_overleaf = ""  # used for overleaf
color = "green"

base_link = f"https://github.com/{user_id}/{repo_name}/blob/{branch_name}/"

# user customized taxonomy
fined_taxonomy = {
    "Conference": ["ACL", "EMNLP", "ACL findings", "EMNLP findings", "NAACL", "COLING", "EACL", "CoNLL", "ICML", "ICLR", "NeurIPS", "AISTATS", "AAAI",
                   "IJCAI", "WWW", "MM", "CVPR", "ICCV", "ECCV", "WACV"],
    
    "Journal": [
        ["TACL", "Transactions of the Association for Computational Linguistics", "Trans. Assoc. Comput. Linguistics"],
        ["TKDE", "IEEE Transactions on Knowledge and Data Engineering", "{IEEE} Trans. Knowl. Data Eng."],
        ["TNNLS", "IEEE Transactions on Neural Networks and Learning Systems",
         "{IEEE} Trans. Neural Networks Learn. Syst."],
        ["IPM", "Information Processing and Managemen", "Inf. Process. Manag."],
        ["KBS", "Knowledge-BasedSystems", "Knowl. Based Syst."]],
    
    "Preprint": ["arXiv", "CoRR"],
    
    # 1: resource type
    "Contribution": ["New Dataset", "Survey", "Important", "New Settings or Metrics", "New Application",
             "Empirical Study", "Theory", "New Pretrained Model", "New Method", "Thesis", "Library", "Workshop",
             "Other Type"],
    # 2: Area
    "Area": ["CV", "NLP", "Multi-Modal", "Robotics"],
    
    # 3: Supervision
    "Supervision": ["Supervised Learning",
                    "Semi-Supervised Learning",
                    "UnSupervised Learning",
                    "Reinforcement Learning",
                    "Other Learning Paradigm"],
    
    # 4: Application
    "Application": ["Image Classification", "Semantic Parsing"],
    
    # 5: Approach
    "Approach": ["Rehearsal", "Regularization", "Dynamic Architecture", "Fast-slow"],
    # 6: Whether need memory
    "Memory": ["w/ External Knowledge", "w/o External Knowledge"],
    
    # 7: Setting
    "Setting": ["Online-learning", "Class-incremental", "Task-incremental"],
    
    # 8: Research Question
    "RQs": {"Few-shot", "Zero-shot", "Imbalanced Data", "Others RQs"},
    
    # 9: Backbone
    "Backbone": ["BERTs", "Transformers", "Adapter", "RNNs", "CNNs", "GNNs", "Attentions", "Capsule Net",
                 "Probabilistic Graphical Model", "VAEs", "Other Structure"],
    
    # 10: Dataset
    "Dataset": ["MNIST", "CIFAR-10",
                "Fashion-MNIST",
                "CIFAR-100",
                "Overnight",
                "NLMapV2",
                "Other Dataset"
                ],
    
    # 11: Metrics
    "Metrics": ["Accuracy", "FWT", "BWT"],
}
