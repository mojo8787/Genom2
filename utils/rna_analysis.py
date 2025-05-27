import pandas as pd
import numpy as np
import random
from typing import Dict, List, Tuple, Optional

def generate_rna_halflife_data(num_genes: int = 20, 
                              seed: int = 42) -> pd.DataFrame:
    """
    Generate synthetic RNA half-life data for demonstration purposes.
    
    Parameters:
    -----------
    num_genes : int
        Number of genes to include in the dataset
    seed : int
        Random seed for reproducibility
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing RNA half-life data for planktonic and biofilm conditions
    """
    np.random.seed(seed)
    
    # Common biofilm-related genes in S. aureus
    gene_pool = [
        "icaA", "icaD", "icaB", "icaC", "sarA", "agrA", "agrC", 
        "fnbA", "fnbB", "clfA", "clfB", "spa", "rbf", "sigB",
        "luxS", "codY", "rot", "mgrA", "sucD", "pgm", "spoVG",
        "saeR", "saeS", "hla", "cidA", "lytS", "lytR", "atl",
        "ebh", "dltA", "dltB", "sdrC", "sasG", "isdA", "isdB",
        "map", "arlR", "arlS", "geh", "lip", "nuc"
    ]
    
    # Ensure we don't request more genes than available
    num_genes = min(num_genes, len(gene_pool))
    
    # Select genes for analysis
    genes = np.random.choice(gene_pool, size=num_genes, replace=False)
    
    # Define gene categories
    categories = {
        "icaA": "EPS production", "icaD": "EPS production", 
        "icaB": "EPS production", "icaC": "EPS production",
        "sarA": "Quorum sensing", "agrA": "Quorum sensing", 
        "agrC": "Quorum sensing", "luxS": "Quorum sensing",
        "fnbA": "Adhesion", "fnbB": "Adhesion", 
        "clfA": "Adhesion", "clfB": "Adhesion", "spa": "Adhesion",
        "sigB": "Stress response", "codY": "Metabolism",
        "rot": "Quorum sensing", "mgrA": "Quorum sensing",
        "sucD": "Metabolism", "pgm": "Metabolism",
        "rbf": "EPS production", "spoVG": "Stress response",
        "saeR": "Quorum sensing", "saeS": "Quorum sensing",
        "hla": "Toxin production", "cidA": "Cell death",
        "lytS": "Autolysis", "lytR": "Autolysis",
        "atl": "Adhesion", "ebh": "Adhesion", 
        "dltA": "Cell wall", "dltB": "Cell wall",
        "sdrC": "Adhesion", "sasG": "Adhesion",
        "isdA": "Iron acquisition", "isdB": "Iron acquisition",
        "map": "Metabolism", "arlR": "Quorum sensing",
        "arlS": "Quorum sensing", "geh": "Metabolism",
        "lip": "Metabolism", "nuc": "Nuclease"
    }
    
    # Generate half-life data with some genes showing higher stability in biofilm
    planktonic_halflife = np.random.uniform(5, 15, len(genes))
    
    # Biofilm factors - some genes will have increased stability in biofilm state
    biofilm_factors = []
    for gene in genes:
        # Genes known to be important for biofilm formation have higher stability
        if gene in ["icaA", "icaB", "icaC", "sarA", "fnbA", "clfA", "rbf", "sasG"]:
            # Higher stability in biofilm
            factor = np.random.uniform(1.8, 4.0)
        elif gene in ["agrA", "agrC", "rot", "hla"]:
            # Lower stability in biofilm
            factor = np.random.uniform(0.3, 0.7)
        else:
            # Random changes
            factor = np.random.uniform(0.7, 2.5)
        
        biofilm_factors.append(factor)
    
    biofilm_halflife = planktonic_halflife * biofilm_factors
    
    # Significant change flag (>1.5x or <0.67x)
    significant = (np.array(biofilm_factors) > 1.5) | (np.array(biofilm_factors) < 0.67)
    
    # Create DataFrame
    data = {
        'gene': genes,
        'category': [categories.get(gene, "Other") for gene in genes],
        'planktonic_halflife': planktonic_halflife,
        'biofilm_halflife': biofilm_halflife,
        'fold_change': biofilm_factors,
        'significant': significant
    }
    
    return pd.DataFrame(data)

def generate_mge_rna_interactions(
    num_interactions: int = 25,
    seed: int = 42
) -> pd.DataFrame:
    """
    Generate synthetic data for MGE-RNA interactions.
    
    Parameters:
    -----------
    num_interactions : int
        Number of interactions to generate
    seed : int
        Random seed for reproducibility
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing MGE-RNA interactions
    """
    random.seed(seed)
    
    # MGE-encoded elements (sRNAs, RNA-binding proteins)
    mge_elements = {
        "SCCmec-sprC": "sRNA",
        "SCCmec-sRNA-42": "sRNA",
        "SCCmec-RBP1": "RNA-binding protein",
        "phiSa3-sRNA-F11": "sRNA",
        "phiSa3-sRNA-A3": "sRNA",
        "phiSa3-RBP3": "RNA-binding protein",
        "ACME-sRNA-A2": "sRNA",
        "ACME-RBP2": "RNA-binding protein",
        "SCCmec-III-RNase": "RNase",
        "phiSa3-Hfq-like": "RNA chaperone"
    }
    
    # Host RNA targets
    host_targets = [
        "icaA-mRNA", "icaR-mRNA", "agrA-mRNA", "sarA-mRNA", 
        "fnbA-mRNA", "clfA-mRNA", "sigB-mRNA", "codY-mRNA",
        "spoVG-mRNA", "rbf-mRNA", "mgrA-mRNA", "saeR-mRNA",
        "lytS-mRNA", "ebh-mRNA", "sasG-mRNA", "rot-mRNA"
    ]
    
    # Define likely interactions and their effects
    # Some MGEs will tend to have specific effects
    mge_biases = {
        "SCCmec-sprC": {"targets": ["icaR-mRNA", "agrA-mRNA"], 
                        "likely_effect": "Degradation", 
                        "biofilm_effect": "Increase"},
        "phiSa3-sRNA-F11": {"targets": ["icaA-mRNA", "sarA-mRNA"], 
                           "likely_effect": "Stabilization", 
                           "biofilm_effect": "Increase"},
        "ACME-sRNA-A2": {"targets": ["fnbA-mRNA", "sasG-mRNA"], 
                         "likely_effect": "Translation control", 
                         "biofilm_effect": "Increase"}
    }
    
    # Generate interactions
    interactions = []
    for _ in range(num_interactions):
        # Select an MGE element
        mge_element = random.choice(list(mge_elements.keys()))
        mge_type = mge_elements[mge_element]
        
        # If this MGE has biases, use them
        if mge_element in mge_biases:
            bias = mge_biases[mge_element]
            # 70% chance to use the biased targets
            if random.random() < 0.7:
                target = random.choice(bias["targets"])
                interaction_type = bias["likely_effect"]
                biofilm_effect = bias["biofilm_effect"]
            else:
                target = random.choice(host_targets)
                interaction_type = random.choice(["Stabilization", "Degradation", "Translation control"])
                biofilm_effect = random.choice(["Increase", "Decrease"])
        else:
            target = random.choice(host_targets)
            # RNA-binding proteins tend to stabilize RNA
            if "RBP" in mge_element:
                interaction_type = random.choices(
                    ["Stabilization", "Translation control", "Degradation"],
                    weights=[0.6, 0.3, 0.1]
                )[0]
            # RNases degrade RNA
            elif "RNase" in mge_element:
                interaction_type = "Degradation"
            # sRNAs can do various things
            else:
                interaction_type = random.choice(["Stabilization", "Degradation", "Translation control"])
            
            # Determine biofilm effect based on target and interaction
            if target in ["icaA-mRNA", "sarA-mRNA", "fnbA-mRNA", "clfA-mRNA", "sasG-mRNA"]:
                # These promote biofilm when expressed
                if interaction_type in ["Stabilization", "Translation control"]:
                    biofilm_effect = "Increase"
                else:
                    biofilm_effect = "Decrease"
            elif target in ["icaR-mRNA", "agrA-mRNA", "rot-mRNA"]:
                # These repress biofilm when expressed
                if interaction_type == "Degradation":
                    biofilm_effect = "Increase"
                else:
                    biofilm_effect = "Decrease"
            else:
                biofilm_effect = random.choice(["Increase", "Decrease"])
        
        # Add confidence score
        confidence = random.uniform(0.6, 0.95)
        
        interactions.append({
            "mge_element": mge_element,
            "mge_type": mge_type,
            "host_target": target,
            "interaction_type": interaction_type,
            "biofilm_effect": biofilm_effect,
            "confidence": confidence
        })
    
    return pd.DataFrame(interactions)

def design_antisense_oligos(target_gene: str, num_designs: int = 3) -> pd.DataFrame:
    """
    Generate synthetic antisense oligonucleotide designs for a target gene.
    
    Parameters:
    -----------
    target_gene : str
        Name of the target gene
    num_designs : int
        Number of designs to generate
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing antisense oligonucleotide designs
    """
    # Generate random sequences (in a real scenario, these would be derived from the actual gene sequence)
    bases = ['A', 'C', 'G', 'U']
    sequences = []
    for _ in range(num_designs):
        seq = ''.join(random.choice(bases) for _ in range(17))
        sequences.append(seq)
    
    # Target regions
    regions = ["5' UTR", "Start codon", f"ORF position {random.randint(100, 500)}-{random.randint(100, 500)}"]
    if len(regions) < num_designs:
        regions.extend([f"ORF position {random.randint(100, 500)}-{random.randint(100, 500)}" 
                        for _ in range(num_designs - len(regions))])
    
    # Generate efficacy scores
    efficacies = [round(random.uniform(0.7, 0.95), 2) for _ in range(num_designs)]
    
    # Generate stability ratings
    stabilities = [random.choice(["High", "Medium", "Low"]) for _ in range(num_designs)]
    
    # Create DataFrame
    data = {
        "sequence": sequences,
        "target_region": regions[:num_designs],
        "efficacy": efficacies,
        "stability": stabilities
    }
    
    return pd.DataFrame(data)

def design_crispr_guides(target_gene: str, num_designs: int = 3) -> pd.DataFrame:
    """
    Generate synthetic CRISPR guide RNA designs for a target gene.
    
    Parameters:
    -----------
    target_gene : str
        Name of the target gene
    num_designs : int
        Number of designs to generate
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing CRISPR guide RNA designs
    """
    # Generate random sequences
    bases = ['A', 'C', 'G', 'U']
    sequences = []
    for _ in range(num_designs):
        seq = ''.join(random.choice(bases) for _ in range(24))
        sequences.append(seq)
    
    # Target regions
    regions = ["5' region", "Middle region", "3' region"]
    if len(regions) < num_designs:
        regions.extend([f"Region {i+4}" for i in range(num_designs - len(regions))])
    
    # Generate efficacy scores
    efficacies = [round(random.uniform(0.7, 0.95), 2) for _ in range(num_designs)]
    
    # Generate off-target information
    off_targets = []
    for _ in range(num_designs):
        if random.random() < 0.7:
            off_targets.append("None detected")
        else:
            num_off = random.randint(1, 2)
            off_target_type = random.choice(["rRNA", "tRNA", "similar gene"])
            off_targets.append(f"{num_off} potential ({off_target_type})")
    
    # Create DataFrame
    data = {
        "sequence": sequences,
        "target_region": regions[:num_designs],
        "predicted_efficacy": efficacies,
        "off_targets": off_targets
    }
    
    return pd.DataFrame(data)

def predict_efficacy_across_lineages(
    target_gene: str, 
    intervention_type: str,
    num_lineages: int = 5,
    seed: int = 42
) -> pd.DataFrame:
    """
    Generate synthetic efficacy predictions across different MRSA lineages.
    
    Parameters:
    -----------
    target_gene : str
        Name of the target gene
    intervention_type : str
        Type of intervention (ASO, CRISPR, etc.)
    num_lineages : int
        Number of lineages to generate predictions for
    seed : int
        Random seed for reproducibility
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing efficacy predictions
    """
    np.random.seed(seed)
    
    # Common MRSA lineages
    lineage_pool = [
        "USA300 (ST8)", "ST239-SCCmecIII", "ST5 (USA100)", 
        "ST22 (EMRSA-15)", "ST1", "ST80", "ST398",
        "ST36 (EMRSA-16)", "ST59", "ST45", "ST30"
    ]
    
    # Select lineages
    lineages = np.random.choice(lineage_pool, size=num_lineages, replace=False)
    
    # Generate baseline efficacy based on target and intervention
    if target_gene in ["icaA", "sarA", "fnbA"]:
        # These are generally good targets
        base_efficacy = 0.8
    else:
        base_efficacy = 0.7
    
    if intervention_type == "Antisense oligonucleotides (ASOs)":
        # ASOs might have more variability
        variance = 0.15
    elif intervention_type == "CRISPR-Cas13 RNA targeting":
        # CRISPR might be more consistent
        variance = 0.1
    else:
        # Small molecules have intermediate variability
        variance = 0.12
    
    # Generate efficacies with some variability
    efficacies = np.random.normal(base_efficacy, variance, num_lineages)
    # Clip to reasonable range
    efficacies = np.clip(efficacies, 0.4, 0.95)
    
    # Create DataFrame
    data = {
        "lineage": lineages,
        "predicted_efficacy": efficacies
    }
    
    return pd.DataFrame(data)

def get_rna_therapeutic_targets() -> pd.DataFrame:
    """
    Return a list of potential RNA therapeutic targets for MRSA biofilm inhibition.
    
    Returns:
    --------
    pd.DataFrame
        DataFrame containing target genes and their characteristics
    """
    targets = [
        {"gene": "icaA", "description": "PIA synthesis, essential for biofilm matrix", 
         "knockdown_effect": "High", "accessibility": "Medium"},
        {"gene": "sarA", "description": "Master regulator of virulence and biofilm", 
         "knockdown_effect": "High", "accessibility": "High"},
        {"gene": "fnbA", "description": "Surface adhesin promoting attachment", 
         "knockdown_effect": "Medium", "accessibility": "High"},
        {"gene": "sprC", "description": "SCCmec-encoded sRNA stabilizing icaA", 
         "knockdown_effect": "High", "accessibility": "Low"},
        {"gene": "RNase Y", "description": "Global RNA degradation machinery", 
         "knockdown_effect": "High", "accessibility": "Low"},
        {"gene": "agrA", "description": "Quorum sensing regulator", 
         "knockdown_effect": "Medium", "accessibility": "Medium"},
        {"gene": "clfA", "description": "Clumping factor promoting adhesion", 
         "knockdown_effect": "Medium", "accessibility": "High"},
        {"gene": "phiSa3-sRNA-F11", "description": "Phage-encoded sRNA affecting host regulation", 
         "knockdown_effect": "High", "accessibility": "Medium"},
        {"gene": "sasG", "description": "Surface protein involved in cell aggregation", 
         "knockdown_effect": "Medium", "accessibility": "High"},
        {"gene": "saeR", "description": "Response regulator affecting virulence", 
         "knockdown_effect": "Medium", "accessibility": "Medium"},
        {"gene": "rbf", "description": "Regulator of biofilm formation", 
         "knockdown_effect": "High", "accessibility": "Medium"},
        {"gene": "cidA", "description": "Cell death and lysis regulator affecting eDNA release", 
         "knockdown_effect": "Medium", "accessibility": "Medium"}
    ]
    
    return pd.DataFrame(targets)

def generate_rna_machinery_data() -> pd.DataFrame:
    """
    Generate synthetic data for RNA degradation machinery expression across different MGE backgrounds.
    
    Returns:
    --------
    pd.DataFrame
        DataFrame containing expression levels of RNA machinery components
    """
    machinery = [
        "RNase III", "RNase Y", "RNase J1", "RNase J2", 
        "PNPase", "RNase R", "Hfq-like", "CshA", "CspA",
        "YhbJ", "RnpA", "CspB", "CspC", "RNA helicase"
    ]
    
    # Generate expression data
    np.random.seed(42)
    planktonic_exp = np.random.uniform(1, 10, len(machinery))
    
    conditions = [
        "SCCmec-II+",
        "SCCmec-III+",
        "phiSa3+",
        "ACME+",
        "SCCmec-II+/phiSa3+",
    ]
    
    data = []
    for machine in machinery:
        base_exp = planktonic_exp[machinery.index(machine)]
        
        row = {
            "machinery": machine,
            "planktonic": base_exp
        }
        
        # Generate fold changes for different MGE conditions
        for condition in conditions:
            if "SCCmec-II" in condition and machine in ["RNase Y", "RNase III", "CshA"]:
                # These are significantly affected by SCCmec-II
                fold_change = np.random.uniform(1.5, 3.0)
            elif "phiSa3" in condition and machine in ["PNPase", "Hfq-like", "CspA"]:
                # These are significantly affected by phiSa3
                fold_change = np.random.uniform(1.5, 3.0)
            elif "ACME" in condition and machine in ["RNase J1", "RNase J2"]:
                # These are significantly affected by ACME
                fold_change = np.random.uniform(0.3, 0.6)  # Downregulated
            else:
                # Random minor changes
                fold_change = np.random.uniform(0.8, 1.2)
            
            row[condition] = base_exp * fold_change
        
        data.append(row)
    
    return pd.DataFrame(data) 